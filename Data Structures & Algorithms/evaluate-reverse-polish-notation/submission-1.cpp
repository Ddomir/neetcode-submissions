#include <cctype>

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> tStack;
        for (const string& c : tokens) {
            if (c == "+") { 
                int a = tStack.top(); tStack.pop();
                int b = tStack.top(); tStack.pop();
                tStack.push(a + b); 
                }
            else if (c == "-") { 
                int a = tStack.top(); tStack.pop();
                int b = tStack.top(); tStack.pop();
                tStack.push(b - a);
                }
            else if (c == "*") { 
                int a = tStack.top(); tStack.pop();
                int b = tStack.top(); tStack.pop();
                tStack.push(a * b); 
            }
            else if (c == "/") { 
                int a = tStack.top(); tStack.pop();
                int b = tStack.top(); tStack.pop();
                tStack.push(b / a); 
            }
            else {
                tStack.push(stoi(c));
            }
        }
        return tStack.top();
    }
};
