using System;
using System.Threading;
using System.Threading.Tasks;

namespace testAsync
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Task<int> value = calleeAsync(1);
            Console.WriteLine("Value: {0}", value.Result);
        }
        private static async Task<int> calleeAsync(int a) 
        {
            await Task.Run(() => Thread.Sleep(5000)
            ) ;
            return a; 
        }

    }
}
