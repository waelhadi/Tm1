import base64

def simple_decrypt(data, key):
    """
    فك التشفير باستخدام XOR مع التحقق من المفتاح.
    """
    # تحقق من صحة المفتاح
    correct_key = "my_secret_key"  # المفتاح الصحيح
    if key != correct_key:
        raise ValueError("⚠️ المفتاح غير صحيح!")

    # فك التشفير باستخدام XOR
    try:
        encrypted = base64.b64decode(data.encode("utf-8")).decode("utf-8")
        decrypted = ''.join(
            chr(ord(c) ^ 42)  # 42 هو ثابت XOR المستخدم في التشفير
            for c in encrypted
        )
        return decrypted
    except Exception as e:
        raise ValueError(f"⚠️ حدث خطأ أثناء فك التشفير: {e}")
