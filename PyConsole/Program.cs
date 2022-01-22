using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PyConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            var fileBytes = File.ReadAllLines(@"C:\Users\dhanasekar.murugesan\source\repos\UnmanagedConsoles\PyConsole\TextFile1.txt");

            foreach (var line in fileBytes)
            {
                int spaceIndex = line.IndexOf('\t');

                var words = line.Split('\t');

                var thriteenltrword = CheckLength(words[0], 13);
                var nineltrword = CheckLength(words[1], 9);

                if(thriteenltrword && nineltrword)
                {
                    continue;
                }
                else
                {
                    Console.WriteLine($"{words[0]} {words[1]}");
                    break;
                }

            }

            Console.ReadLine();
        }

        static bool CheckLength(string str, int maxLen)
        {
            return !string.IsNullOrEmpty(str) && str.Length == maxLen;
        }
    }
}
