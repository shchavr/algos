using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

class Program
{
    static void Main()
    {
        BigInt a = new BigInt(1234563);
        BigInt b = new BigInt(41245);

        BigInt sum = a + b; 
        BigInt difference = a - b; 
        BigInt product = a * b; 
        BigInt quotient = a / b; 
        BigInt remainder = a % b; 

        Console.WriteLine($"a + b = {sum}");
        Console.WriteLine($"a - b = {difference}");
        Console.WriteLine($"a * b = {product}");
        Console.WriteLine($"a / b = {quotient}");
        Console.WriteLine($"a % b = {remainder}");

        Console.WriteLine($"a == b: {a == b}");
        Console.WriteLine($"a != b: {a != b}");
        Console.WriteLine($"a < b: {a < b}");
        Console.WriteLine($"a > b: {a > b}");

        try
        {
            BigInt inverse = a.InverseModulo(b);
            Console.WriteLine($"Обратное a по модулю b: {inverse}");
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine(ex.Message);
        }

        Console.ReadLine(); 

        
        long n, e, dKey; // Переименовали переменную d в dKey, чтобы избежать конфликта имен
        RSA.GenerateKeys(out n, out e, out dKey);

        
        Console.WriteLine($"Открытый ключ (e, n): ({e}, {n})");
        Console.WriteLine($"Закрытый ключ (d, n): ({dKey}, {n})");

        
        string inputFile = "input.txt"; 
        string encryptedFile = "encrypted.txt"; 
        string outputFile = "output.txt"; 

        
        string text = File.ReadAllText(inputFile, Encoding.UTF8);
        Console.WriteLine($"Исходный текст: {text}");

       
        List<long> encrypted = new List<long>(); 
        foreach (char c in text) 
        {
            long m = (long)c; 
            long ciphered = RSA.Encrypt(m, e, n); 
            encrypted.Add(ciphered); 
        }

        using (StreamWriter writer = new StreamWriter(encryptedFile))
        {
            foreach (long c in encrypted)
            {
                writer.Write(c + " ");
            }
        }

        Console.WriteLine("Зашифрованный текст:");
        foreach (long c in encrypted)
            Console.Write(c + " ");
        Console.WriteLine();

        
        StringBuilder decryptedText = new StringBuilder(); 
        foreach (long c in encrypted) 
        {
            long m = RSA.Decrypt(c, dKey, n); 
            decryptedText.Append((char)m); 
        }

        Console.WriteLine($"Расшифрованный текст: {decryptedText}");

        File.WriteAllText(outputFile, decryptedText.ToString(), Encoding.UTF8);

        Console.ReadLine(); 
    }
}