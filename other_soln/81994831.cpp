#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long house_n, task_n, s=0;
    cin>> house_n>> task_n;
    vector<long long >tasks;
    for(int i=0;i<task_n;i++) {
        int x;
        cin>>x;
        tasks.push_back(x);
    }
    s = tasks[0]-1;
    for(int i=0;i<task_n-1;i++) {
        if(tasks[i+1]>=tasks[i])
            s += tasks[i+1]-tasks[i];
        else s += house_n-tasks[i]+tasks[i+1];
    }
    cout<<s<<endl;
}