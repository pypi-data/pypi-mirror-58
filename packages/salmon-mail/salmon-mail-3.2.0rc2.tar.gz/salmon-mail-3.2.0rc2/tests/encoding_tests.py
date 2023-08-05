# -*- coding: utf-8 -*-
from email import encoders
from email.utils import parseaddr
import mailbox
import os

from mock import Mock, patch
import chardet

from salmon import encoding

from .setup_env import SalmonTestCase

BAD_HEADERS = [
    '"\u8003\u53d6\u5206\u4eab" <Ernest.Beard@msa.hinet.net>',
    '"=?windows-1251?B?RXhxdWlzaXRlIFJlcGxpY2E=?="\n\t<wolfem@barnagreatlakes.com>',
    '=?iso-2022-jp?B?Zmlicm91c19mYXZvcmF0ZUB5YWhvby5jby5qcA==?=<fibrous_favorate@yahoo.co.jp>',

    '=?windows-1252?Q?Global_Leadership_in_HandCare_-_Consumer,\n\t_Professional_and_Industrial_Products_OTC_:_FLKI?=',
    '=?windows-1252?q?Global_Leadership_in_Handcare_-_Consumer, _Auto,\n\t_Professional_&_Industrial_Products_-_OTC_:_FLKI?=',  # noqa
    'I am just normal.',
    '=?koi8-r?B?WW91ciBtYW6ScyBzdGFtaW5hIHdpbGwgY29tZSBiYWNrIHRvIHlvdSBs?=\n\t=?koi8-r?B?aWtlIGEgYm9vbWVyYW5nLg==?=',
    '=?koi8-r?B?WW91IGNhbiBiZSBvbiB0b3AgaW4gYmVkcm9vbSBhZ2FpbiCWIGp1c3Qg?=\n\t=?koi8-r?B?YXNrIHVzIGZvciBhZHZpY2Uu?=',
    '"=?koi8-r?B?5MXMz9DSz8na18/E09TXzw==?=" <daniel@specelec.com>',
    '=?utf-8?b?IumrlOiCsuWckuWNgOermSDihpIg6ZW35bqa6Yar6Zmi56uZIOKGkiDmlofljJbk?=\n =?utf-8?b?uInot6/nq5kiIDx2Z3hkcmp5Y2lAZG5zLmh0Lm5ldC50dz4=?=',  # noqa: E501
    '=?iso-8859-1?B?SOlhdnkgTel05WwgVW7uY/hk?=\n\t=?iso-8859-1?Q?=E9?=',
]

DECODED_HEADERS = encoding.header_from_mime_encoding(BAD_HEADERS)

NORMALIZED_HEADERS = [encoding.header_to_mime_encoding(x) for x in DECODED_HEADERS]


class EncodingTestCase(SalmonTestCase):
    def test_MailBase(self):
        the_subject = u'p\xf6stal'
        m = encoding.MailBase()

        m['To'] = "testing@localhost"
        m['Subject'] = the_subject
        m['Content-Type'] = 'text/plain; charset=iso-8859-1'
        m['MIME-Version'] = '1.0'

        self.assertEqual(m['To'], "testing@localhost")
        self.assertEqual(m['TO'], m['To'])
        self.assertEqual(m['to'], m['To'])

        self.assertEqual(m['Subject'], the_subject)
        self.assertEqual(m['subject'], m['Subject'])
        self.assertEqual(m['sUbjeCt'], m['Subject'])

        msg = encoding.to_message(m)
        m2 = encoding.from_message(msg)

        self.assertEqual(len(m), len(m2))

        self.assertEqual(m.items(), m2.items())

        for k in m:
            assert m[k] == m2[k], "%s: %r != %r" % (k, m[k], m2[k])

        assert("To" in m)
        assert("Bob" not in m)
        self.assertEqual(m["To"], "testing@localhost")
        m["To"] = "somebody@localhost"
        self.assertEqual(m["To"], "somebody@localhost")
        self.assertEqual(m.keys(), ['Subject', 'Mime-Version', 'Content-Type', 'To'])
        self.assertEqual(m.items(), [
            ('Subject', the_subject),
            ('Mime-Version', '1.0'),
            ('Content-Type', 'text/plain; charset="iso-8859-1"'),
            ('To', 'somebody@localhost')])
        self.assertEqual(m.get_all("Subject"), [the_subject])
        self.assertEqual(m.get_all("Bob"), [])

        # appending headers
        m.append_header("subject", "something else")
        self.assertEqual(m["Subject"], the_subject)
        self.assertEqual(m.keys(), ['Subject', 'Mime-Version', 'Content-Type', 'To', "Subject"])
        self.assertEqual(m.items(), [
            ('Subject', the_subject),
            ('Mime-Version', '1.0'),
            ('Content-Type', 'text/plain; charset="iso-8859-1"'),
            ('To', 'somebody@localhost'),
            ('Subject', "something else")])
        self.assertEqual(m.get_all("Subject"), [the_subject, "something else"])

        # reset subject header
        m["Subject"] = the_subject

        for key, item in zip(m.keys(), m.items()):
            self.assertEqual(key, item[0])
            assert key in m
            del m[key]
            assert key not in m
            assert key not in [i[0] for i in m.items()]

    def test_normalized_headers(self):
        base = encoding.MailBase()

        # __setitem__ will normalize headers when they're added
        base["subJect"] = "test"
        self.assertEqual(base["Subject"], "test")
        self.assertEqual(base.mime_part["Subject"], "test")
        self.assertEqual(base.keys(), ["Subject"])
        self.assertEqual(base.mime_part.keys(), ["Subject"])

        # if the header wasn't added via __setitem__, it should still be returned
        # to Salmon users in a normalized form
        base.mime_part["fRom"] = "test@example.com"
        self.assertEqual(base["From"], "test@example.com")
        self.assertEqual(base.mime_part["fRom"], "test@example.com")
        self.assertEqual(base.keys(), ["Subject", "From"])
        self.assertEqual(base.mime_part.keys(), ["Subject", "fRom"])

    def test_header_to_mime_encoding(self):
        for i, header in enumerate(DECODED_HEADERS):
            self.assertEqual(NORMALIZED_HEADERS[i], encoding.header_to_mime_encoding(header))

    def test_mutt_badness(self):
        # this is a sample of possibly the worst case Mutt can produce
        idiot = '=?iso-8859-1?B?SOlhdnkgTel05WwgVW7uY/hk?=\n\t=?iso-8859-1?Q?=E9?='
        should_be = u'H\xe9avy M\xe9t\xe5l Un\xeec\xf8d\xe9'
        self.assertEqual(encoding.header_from_mime_encoding(idiot), should_be)

    def test_header_from_mime_encoding(self):
        assert not encoding.header_from_mime_encoding(None)
        self.assertEqual(len(BAD_HEADERS), len(encoding.header_from_mime_encoding(BAD_HEADERS)))

        for i, header in enumerate(BAD_HEADERS):
            self.assertEqual(DECODED_HEADERS[i], encoding.header_from_mime_encoding(header))

    def test_to_message_from_message_with_spam(self):
        mb = mailbox.mbox("tests/data/spam")

        for msg in mb:
            m = encoding.from_message(msg)
            out = encoding.to_message(m)
            assert repr(out)

            m2 = encoding.from_message(out)

            for k in m:
                if '@' in m[k]:
                    self.assertEqual(parseaddr(m[k]), parseaddr(m2[k]))
                elif k.lower() in [key.lower() for key in encoding.CONTENT_ENCODING_KEYS]:
                    pass  # skip!
                else:
                    assert m[k].strip() == m2[k].strip(), "%s: %r != %r" % (k, m[k], m2[k])

                assert not m[k].startswith(u"=?")
                assert not m2[k].startswith(u"=?")

            # salmon adds stuff to content headers that's missing from example messages
            for k in encoding.CONTENT_ENCODING_KEYS:
                if k == "Content-Transfer-Encoding" \
                        and m.content_encoding[k][0] is None \
                        and m2.content_encoding[k][0] == "7bit":
                    continue  # salmon fixing bad email
                elif k == "Mime-Version" \
                        and m.content_encoding[k][0] is None \
                        and m2.content_encoding[k][0] == "1.0":
                    continue  # again, salmon fixing bad email

                assert m.content_encoding[k][0] == m2.content_encoding[k][0], \
                    "%s: %r != %r" % (k, m.content_encoding[k], m2.content_encoding[k])

                for p in m.content_encoding[k][1]:
                    if p in m2.content_encoding[k][1]:
                        assert m.content_encoding[k][1][p].lower() == m2.content_encoding[k][1][p].lower(), \
                            "%s: %r != %r" % (p, m.content_encoding[k][1][p], m2.content_encoding[k][1][p])

            assert m.body == m2.body, "Bodies don't match"

            self.assertEqual(len(m.parts), len(m2.parts), "Not the same number of parts.")

            for i, part in enumerate(m.parts):
                assert part.body == m2.parts[i].body, \
                    "Part %d isn't the same: %r \nvs\n. %r" % (i, part.body, m2.parts[i].body)

    def test_to_file_from_file(self):
        mb = mailbox.mbox("tests/data/spam")
        msg = encoding.from_message(mb[0])

        outfile = "run/encoding_test.msg"

        with open(outfile, 'w') as outfp:
            encoding.to_file(msg, outfp)

        with open(outfile) as outfp:
            msg2 = encoding.from_file(outfp)

        self.assertEqual(len(msg), len(msg2))
        os.unlink(outfile)

    def test_guess_encoding_and_decode(self):
        for header in DECODED_HEADERS:
            try:
                encoding.guess_encoding_and_decode('ascii', header.encode('utf-8'))
            except encoding.EncodingError:
                pass

    def test_attempt_decoding(self):
        for header in DECODED_HEADERS:
            encoding.attempt_decoding('ascii', header.encode('utf-8'))

    def test_properly_decode_header(self):
        for i, header in enumerate(BAD_HEADERS):
            parsed = encoding.properly_decode_header(header)
            self.assertEqual(DECODED_HEADERS[i], parsed)

    def test_headers_round_trip(self):
        # round trip the headers to make sure they convert reliably back and forth
        for header in BAD_HEADERS:
            original = encoding.header_from_mime_encoding(header)

            assert original
            assert "=?" not in original and "?=" not in original, "Didn't decode: %r" % header

            encoded = encoding.header_to_mime_encoding(original)
            assert encoded

            return_original = encoding.header_from_mime_encoding(encoded)
            self.assertEqual(original, return_original)

            return_encoded = encoding.header_to_mime_encoding(return_original)
            self.assertEqual(encoded, return_encoded)

    def test_MIMEPart(self):
        text1 = encoding.MIMEPart("text/plain")
        text1.set_payload("The first payload.")
        text2 = encoding.MIMEPart("text/plain")
        text2.set_payload("The second payload.")

        with open("tests/data/salmon.png", "rb") as file_obj:
            image_data = file_obj.read()
        img1 = encoding.MIMEPart("image/png")
        img1.set_payload(image_data)
        img1.set_param('attachment', '', header='Content-Disposition')
        img1.set_param('filename', 'salmon.png', header='Content-Disposition')
        encoders.encode_base64(img1)

        multi = encoding.MIMEPart("multipart/mixed")
        for x in [text1, text2, img1]:
            multi.attach(x)

        mail = encoding.from_message(multi)

        self.assertEqual(mail.parts[0].body, "The first payload.")
        self.assertEqual(mail.parts[1].body, "The second payload.")
        self.assertEqual(mail.parts[2].body, image_data)

        encoding.to_message(mail)

    @patch('chardet.detect', new=Mock())
    def test_guess_encoding_fails_completely(self):
        chardet.detect.return_value = {'encoding': None, 'confidence': 0.0}
        with self.assertRaises(encoding.EncodingError):
            encoding.guess_encoding_and_decode('ascii', 'some data', errors='strict')

    def test_attach_text(self):
        mail = encoding.MailBase()
        mail.attach_text("This is some text.", 'text/plain')

        msg = encoding.to_message(mail)
        self.assertEqual(msg.get_payload(0).get_payload(), "This is some text.")
        assert encoding.to_string(mail)

        mail.attach_text("<html><body><p>Hi there.</p></body></html>", "text/html")
        msg = encoding.to_message(mail)
        self.assertEqual(len(msg.get_payload()), 2)
        assert encoding.to_string(mail)

    def test_attach_file(self):
        mail = encoding.MailBase()
        with open("tests/data/salmon.png", "rb") as file_obj:
            png = file_obj.read()
        mail.attach_file("salmon.png", png, "image/png", "attachment")
        msg = encoding.to_message(mail)

        payload = msg.get_payload(0)
        self.assertEqual(payload.get_payload(decode=True), png)
        self.assertEqual(payload.get_filename(), "salmon.png")

    def test_content_encoding_headers_are_maintained(self):
        with open("tests/data/signed.msg", "rb") as file_obj:
            inmail = encoding.from_file(file_obj)

        ctype, ctype_params = inmail.content_encoding['Content-Type']

        self.assertEqual(ctype, 'multipart/signed')

        # these have to be maintained
        for key in ['protocol', 'micalg']:
            assert key in ctype_params

        # these get removed
        for key in encoding.CONTENT_ENCODING_REMOVED_PARAMS:
            assert key not in ctype_params

        outmsg = encoding.to_message(inmail)
        ctype, ctype_params = encoding.parse_parameter_header(outmsg, 'Content-Type')
        for key in ['protocol', 'micalg']:
            assert key in ctype_params, key

    def test_odd_content_type_with_charset(self):
        mail = encoding.MailBase()
        mail.body = u"p\xf6stal".encode('utf-8')
        mail.content_encoding['Content-Type'] = ('application/plain', {'charset': 'utf-8'})

        msg = encoding.to_string(mail)
        assert msg

    def test_specially_borked_lua_message(self):
        with open("tests/data/borked.msg", "rb") as file_obj:
            msg = encoding.from_file(file_obj)
        assert msg

    @patch('salmon.encoding.MIMEPart.__init__')
    def test_to_message_encoding_error(self, mp_init):
        mp_init.side_effect = TypeError
        with open("tests/data/borked.msg", "rb") as file_obj:
            test = encoding.from_file(file_obj)
        with self.assertRaises(encoding.EncodingError):
            encoding.to_message(test)

    @patch('salmon.encoding.chardet.detect')
    def test_guess_encoding_and_decode_unicode_error(self, detect_mock):
        data = u"testß".encode("latin-1")
        detect_mock.return_value = {"confidence": 0.99, "encoding": "utf-8"}
        with self.assertRaises(encoding.EncodingError):
            encoding.guess_encoding_and_decode("ascii", data)

    def test_attempt_decoding_with_bad_encoding_name(self):
        self.assertEqual("test", encoding.attempt_decoding("asdfasdf", "test"))

    def test_apply_charset_to_header_with_bad_encoding_char(self):
        with self.assertRaises(encoding.EncodingError):
            encoding.apply_charset_to_header('ascii', 'X', 'bad')

    def test_odd_roundtrip_bug(self):
        decoded_addrs = [
                u'"\u0414\u0435\u043b\u043e\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e" <daniel@specelec.com>',  # noqa: E501
            u'"\u8003\u53d6\u5206\u4eab" <Ernest.Beard@msa.hinet.net>',
            u'"Exquisite Replica"\n\t<wolfem@barnagreatlakes.com>',
        ]

        for decoded in decoded_addrs:
            encoded = encoding.header_to_mime_encoding(decoded)
            assert '<' in encoded and '"' in encoded, "Address wasn't encoded correctly:\n%s" % encoded

    def test_multiple_headers(self):
        msg = encoding.MailBase()
        msg["To"] = "somedude@localhost"
        msg["From"] = "nobody@localhost"
        assert("From" in msg)
        self.assertEqual(msg["From"], "nobody@localhost")
        msg["From"] = "somebody@localhost"
        self.assertEqual(msg["From"], "somebody@localhost")
        self.assertEqual(msg.keys(), ["To", "From"])

        # appending headers
        msg.append_header("To", "nobody@example.com")
        self.assertEqual(msg["To"], "somedude@localhost")
        self.assertEqual(msg.keys(), ["To", "From", "To"])
