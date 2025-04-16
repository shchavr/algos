using System;
using System.Linq;

public class BigInt
{
    private byte[] _bytes;

    // Конструктор по умолчанию
    public BigInt()
    {
        _bytes = new byte[8];
    }

    // Конструктор из long
    public BigInt(long value)
    {
        _bytes = BitConverter.GetBytes(value);
    }

    // Конструктор из массива байт
    public BigInt(byte[] bytes)
    {
        if (bytes.Length != 8)
            throw new ArgumentException("Массив байт должен иметь длину 8.");
        _bytes = bytes.ToArray();
    }

    // Преобразование в long
    public long ToLong()
    {
        return BitConverter.ToInt64(_bytes, 0);
    }

    // Перегрузка оператора сложения с проверкой переполнения
    public static BigInt operator +(BigInt a, BigInt b)
    {
        try
        {
            long result = checked(a.ToLong() + b.ToLong());
            return new BigInt(result);
        }
        catch (OverflowException)
        {
            throw new OverflowException("Переполнение при сложении.");
        }
    }

    // Перегрузка оператора вычитания с проверкой переполнения
    public static BigInt operator -(BigInt a, BigInt b)
    {
        try
        {
            long result = checked(a.ToLong() - b.ToLong());
            return new BigInt(result);
        }
        catch (OverflowException)
        {
            throw new OverflowException("Переполнение при вычитании.");
        }
    }

    // Перегрузка оператора умножения с проверкой переполнения
    public static BigInt operator *(BigInt a, BigInt b)
    {
        try
        {
            long result = checked(a.ToLong() * b.ToLong());
            return new BigInt(result);
        }
        catch (OverflowException)
        {
            throw new OverflowException("Переполнение при умножении.");
        }
    }

    // Перегрузка оператора деления
    public static BigInt operator /(BigInt a, BigInt b)
    {
        if (b.ToLong() == 0)
            throw new DivideByZeroException("Деление на ноль.");
        long result = a.ToLong() / b.ToLong();
        return new BigInt(result);
    }

    // Перегрузка оператора взятия остатка
    public static BigInt operator %(BigInt a, BigInt b)
    {
        if (b.ToLong() == 0)
            throw new DivideByZeroException("Деление на ноль при взятии остатка.");
        long result = a.ToLong() % b.ToLong();
        return new BigInt(result);
    }

    // Перегрузка оператора равенства
    public static bool operator ==(BigInt a, BigInt b)
    {
        return a.ToLong() == b.ToLong();
    }

    // Перегрузка оператора неравенства
    public static bool operator !=(BigInt a, BigInt b)
    {
        return a.ToLong() != b.ToLong();
    }

    // Перегрузка оператора меньше
    public static bool operator <(BigInt a, BigInt b)
    {
        return a.ToLong() < b.ToLong();
    }

    // Перегрузка оператора больше
    public static bool operator >(BigInt a, BigInt b)
    {
        return a.ToLong() > b.ToLong();
    }

    // Метод для взятия обратного по модулю
    public BigInt InverseModulo(BigInt modulo)
    {
        long a = this.ToLong();
        long m = modulo.ToLong();
        long x, y;
        long g = ExtendedGCD(a, m, out x, out y);
        if (g != 1)
            throw new InvalidOperationException("Обратного элемента не существует.");
        return new BigInt((x % m + m) % m);
    }

    // Расширенный алгоритм Евклида для нахождения НОД и коэффициентов Безу
    private static long ExtendedGCD(long a, long b, out long x, out long y)
    {
        if (a == 0)
        {
            x = 0;
            y = 1;
            return b;
        }
        long x1, y1;
        long gcd = ExtendedGCD(b % a, a, out x1, out y1);
        x = y1 - (b / a) * x1;
        y = x1;
        return gcd;
    }

    // Переопределение метода Equals
    public override bool Equals(object obj)
    {
        if (obj is BigInt)
        {
            return this == (BigInt)obj;
        }
        return false;
    }

    // Переопределение метода GetHashCode
    public override int GetHashCode()
    {
        return ToLong().GetHashCode();
    }

    // Переопределение метода ToString
    public override string ToString()
    {
        return ToLong().ToString();
    }
}
