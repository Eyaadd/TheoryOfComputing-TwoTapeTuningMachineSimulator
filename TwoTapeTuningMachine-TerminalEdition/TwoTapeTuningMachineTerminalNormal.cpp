
#include <iostream>
#include <vector>

using namespace std;

void printTapes(const vector<char>& tape1, const vector<char>& tape2, int head1, int head2) {
    cout << "Tape 1: ";
    for (char c : tape1) {
        cout << c << ' ';
    }
    cout << endl << "       ";
    for (int i = 0; i < head1; i++) {
        cout << "  ";
    }
    cout << "^ Head 1" << endl;

    cout << "Tape 2: ";
    for (char c : tape2) {
        cout << c << ' ';
    }
    cout << endl << "       ";
    for (int i = 0; i < head2; i++) {
        cout << "  ";
    }
    cout << "^ Head 2" << endl;
}

int main() {
    vector<char> tape1 = {'B','a','a','b','c','a','a','b','B'};
    vector<char> tape2 ={'B'};      
    int head1 = 1;
    int head2 = 1;
    while(true) {
        while (head1 < tape1.size() && (tape1[head1] == 'a' || tape1[head1] == 'b')) {
            tape2.push_back(tape1[head1]);
            head1++;
            head2++;
            printTapes(tape1, tape2, head1, head2);
        }
        tape2.push_back('B');

        if (head1 < tape1.size() && tape1[head1] == 'c') {
            head1++;

            head2 = 0;
            head2++;
            
            bool flag = false;
            while(tape1[head1] == tape2[head2]) {
                if(tape1[head1]=='B'&&tape2[head2]=='B'){
                    flag = true;
                    break;   
                }
                head1++;
                head2++;
                
            }
            if (flag) {
                cout << "Language succeeded" << endl;
                break;
            } else {
                cout << "Language denied" << endl;
                break;
            }
            break;
        } else {
            cout << "Language denied" << endl;
            break;
        }
    }

    return 0;
}
