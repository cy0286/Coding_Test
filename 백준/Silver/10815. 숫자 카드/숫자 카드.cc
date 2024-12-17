#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <map> //key와 value가 한 쌍으로, 중복 허용 x
using namespace std;

int main()
{
    map<int, int>map1; //map<key type, value type>이름
    //map<int, int>map2;
    int N; //숫자 카드의 개수
    int n; //숫자 카드에 적혀있는 수
    //int M; //정수의 개수
    //int m; //정수
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &n);
        map1[n] = 1;
    }
    scanf("%d", &N);
    for(int j = 0; j <N; j++)
        {
            scanf("%d", &n);
            if (map1[n])
            {
                cout << "1 ";
            }
            else
            {
                cout << "0 ";
            }
        }
    return 0;
}