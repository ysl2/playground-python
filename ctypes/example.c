// example.c
//
// Linux/macOS:
// clang -shared -o example.so example.c
// Windows:
// clang -shared -o example.dll example.c

long long example(int x)
{
    long long y;
    long long i;
    int j;

    for (j = 0; j < x; j++)
    {
        y = 0;
        for (i = 0; i < x; i++)
        {
            y += i * i;
        }
    }

    return y;
}
