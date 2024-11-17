import base64

def simple_decrypt(data, secret_key):
    """
    فك التشفير باستخدام XOR مع المفتاح السري.
    """
    try:
        # تحويل البيانات المشفرة من Base64 إلى النص الأصلي
        encrypted = base64.b64decode(data.encode("utf-8")).decode("utf-8")

        # فك التشفير باستخدام XOR
        decrypted = ''.join(
            chr(ord(c) ^ ord(k))
            for c, k in zip(encrypted, secret_key * (len(encrypted) // len(secret_key) + 1))
        )
        return decrypted
    except Exception as e:
        raise ValueError(f"⚠️ حدث خطأ أثناء فك التشفير: {e}")
