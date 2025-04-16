public class RSA
{
    // Генерация ключей
    public static void GenerateKeys(out long n, out long e, out long d)
    {
        long p = 997;
        long q = 991;
        n = p * q;
        long phi = (p - 1) * (q - 1);
        e = 65537;
        d = ModInverse(e, phi);
    }

    // Шифрование сообщения
    public static long Encrypt(long m, long e, long n)
    {
        return ModPow(m, e, n);
    }

    // Расшифрование сообщения
    public static long Decrypt(long c, long d, long n)
    {
        return ModPow(c, d, n);
    }

    // Возведение в степень по модулю
    private static long ModPow(long m, long e, long n)
    {
        long result = 1;
        m = m % n;
        while (e > 0)
        {
            if ((e & 1) == 1)
                result = (result * m) % n;
            e = e >> 1;
            m = (m * m) % n;
        }
        return result;
    }

    // Вычисление обратного элемента по модулю
    private static long ModInverse(long e, long phi)
    {
        long m0 = phi;
        long y = 0, x = 1;
        if (phi == 1)
            return 0;
        while (e > 1)
        {
            long q = e / phi;
            long t = phi;
            phi = e % phi;
            e = t;
            t = y;
            y = x - q * y;
            x = t;
        }
        if (x < 0)
            x += m0;
        return x;
    }
}