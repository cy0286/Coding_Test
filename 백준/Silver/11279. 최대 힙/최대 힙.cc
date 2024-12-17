#include <iostream>
#include <queue> //priority_queue
using namespace std;

int main() 
{
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    priority_queue<int, vector<int>> pq;
    int n;
    cin >> n;

    while (n--) 
    {
        int x;
        cin >> x;

        if (x) 
        {
            pq.push(x);
        }
        else 
        {
            if (!pq.empty()) 
            {
                cout << pq.top() << '\n';
                pq.pop();
            }
            else
                cout << 0 << '\n';
        }
    }
    return 0;
}