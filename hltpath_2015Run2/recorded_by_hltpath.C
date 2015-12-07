// Code by Emilien : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/2627/1/1.html
// First make a binary of this program 
// Run using the following command : 
// ./recorded_by_hltpath_fromDQM --type Datasets --human --minrun 262548
// ./recorded_by_hltpath_fromDQM --type HLT --hlttype accept --minrun 262548

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>
#include <vector>
#include <set>

using namespace std;


// PURPOSE
// This is a simple program counting the number of events having been recorded for each HLT path, given a list of input files
//
// The output is formatted as follows:
// HLT path nLS L1Pass PSPass PAccept
//
// USAGE:
// recorded_by_hltpath [-h|--help] [--nLS] [--L1Pass] [--PSPass] [--PAccept] [pattern1 [pattern2 [...]]]
// -h, --help: display the help
// --nLS: print the number of lumi sections
// --L1Pass: print the L1 accept
// --PSPass: print the HLT accept (before PS)
// --PAccept: print the HLT accept (after PS)
// pattern1, pattern2, ...: optional pattern(s). If provided, the HLT paths mathing each of these pattern(s) will be combined. Otherwise, all HLT paths are printed individually.
//
// If none of --nLS, --L1Pass, --PSPass or --PAccept are provided, all numbers are printed (default).
//
// CAUTION: this program does not know anything about overlaps.

string basedir = "/afs/cern.ch/user/e/echapon/workspace/public/RunPrep2015/HLT_runbyrun";

int main(int argc, const char** argv) {
   if (argc==2 && (string(argv[1]) == "-h" || string(argv[1]) == "--help")) {
      cout << " PURPOSE" << endl;
      cout << " This is a simple program counting the number of events having been recorded for each HLT path, given a list of input files" << endl;
      cout << "" << endl;
      cout << " The output is formatted as follows:" << endl;
      cout << " HLT path nLS L1Pass PSPass PAccept" << endl;
      cout << "" << endl;
      cout << " USAGE:" << endl;
      cout << " recorded_by_hltpath [-h|--help] [--nLS] [--L1Pass] [--PSPass] [--PAccept] [pattern1 [pattern2 [...]]]" << endl;
      cout << " -h, --help: display the help" << endl;
      cout << " --nLS: print the number of lumi sections" << endl;
      cout << " --L1Pass: print the L1 accept" << endl;
      cout << " --PSPass: print the HLT accept (before PS)" << endl;
      cout << " --PAccept: print the HLT accept (after PS)" << endl;
      cout << " pattern1, pattern2, ...: optional pattern(s). If provided, the HLT paths mathing each of these pattern(s) will be combined. Otherwise, all HLT paths are printed individually." << endl;
      cout << "" << endl;
      cout << " If none of --nLS, --L1Pass, --PSPass or --PAccept are provided, all numbers are printed (default)." << endl;
      cout << "" << endl;
      cout << " CAUTION: this program does not know anything about overlaps." << endl;
      return 1;
   }
   // list of runs and lumis to process... hardcoded for now
   const int nruns = 18;
   int run[nruns] = {
      262548, 262563, 262620, 262640, 262656,
      262694, 262695, 262697, 262698, 262699,
      262701, 262702, 262703, 262726, 262733,
      262734, 262735, 262784
   };
   int lumistart[nruns] = {
      100, 1, 98, 86, 1,
      71, 1, 1, 1, 1,
      1, 1, 1, 64, 61,
      1, 1, 1
   };
   int lumiend[nruns] = {
      368, 79, 423, 241, 178,
      229, 227, 63, 18, 48,
      9, 10, 123, 506, 87,
      10, 206, 374
   };
   bool process[nruns] = {
      true, true, true, true, true,
      true, true, true, true, true,
      true, true, true, true, true,
      true, true, true
   };

   // if the user gave us some strings, we'll use them to group triggers together
   // also check for flags
   vector<string> user_paths;
   bool print_nLS = false;
   bool print_L1Pass = false;
   bool print_PSPass = false;
   bool print_PAccept = false;
   for (int i=1; i<argc; i++) {
      string arg(argv[i]);
      if (arg=="--nLS") print_nLS = true;
      else if (arg=="--L1Pass") print_L1Pass = true;
      else if (arg=="--PSPass") print_PSPass = true;
      else if (arg=="--PAccept") print_PAccept = true;
      else user_paths.push_back(arg);
   }
   if (!print_nLS && !print_L1Pass && !print_PSPass && !print_PAccept) {
      print_nLS = true; print_L1Pass = true; print_PSPass = true; print_PAccept = true;
   }

   map<string, int> map_nLS, map_L1Pass, map_PSPass, map_PAccept;
   map<string, int> map_nLS_user, map_L1Pass_user, map_PSPass_user, map_PAccept_user;

   // loop on the runs
   for (int i=0; i<nruns; i++) {
      if (!process[i]) continue;

      ostringstream oss;
      oss << basedir << "/" << run[i] << "_LS_" << lumistart[i] << "_" << lumiend[i] << ".txt";
      ifstream file(oss.str().c_str());
      if (!file.is_open()) {
         cout << "Error opening " << oss.str() << endl;
         continue;
      }

      string hltpath, dummy; int nLS, L1Pass, PSPass, PAccept;
      string line;
      set<string> found_user;
      while (getline(file,line)) {
         istringstream ss(line);
         ss >> dummy >> hltpath >> dummy  >> nLS >> dummy >> L1Pass >> PSPass >> PAccept;
         map_nLS[hltpath] += nLS;
         map_L1Pass[hltpath] += L1Pass;
         map_PSPass[hltpath] += PSPass;
         map_PAccept[hltpath] += PAccept;

         // does the hltpath match a pattern given by the user?
         for (vector<string>::iterator it = user_paths.begin(); it != user_paths.end(); it++) {
            if (hltpath.find(*it)!=string::npos) {
               if (found_user.find(*it) == found_user.end()) {
                  map_nLS_user[*it] += nLS;
                  found_user.insert(*it);
               }
               map_L1Pass_user[*it] += L1Pass;
               map_PSPass_user[*it] += PSPass;
               map_PAccept_user[*it] += PAccept;
            }
         }
      }
      file.close();
   }

   // print results

   if (user_paths.size()==0) {
      map<string, int>::iterator it_nLS = map_nLS.begin();
      map<string, int>::iterator it_L1Pass = map_L1Pass.begin();
      map<string, int>::iterator it_PSPass = map_PSPass.begin();
      map<string, int>::iterator it_PAccept = map_PAccept.begin();
      cout << "HLT path\t\t";
      if (print_nLS) cout << "nLS\t\t";
      if (print_L1Pass) cout << "L1Pass\t\t";
      if (print_PSPass) cout << "PSPass\t\t";
      if (print_PAccept) cout << "PAccept";
      cout << endl;
      for (it_nLS = map_nLS.begin(); it_nLS != map_nLS.end(); it_nLS++) {
         cout << it_nLS->first << "\t";
         if (print_nLS) cout << it_nLS->second << "\t";
         if (print_L1Pass) cout << it_L1Pass->second << "\t";
         if (print_PSPass) cout << it_PSPass->second << "\t";
         if (print_PAccept) cout << it_PAccept->second;
         cout << endl;
         it_L1Pass++;
         it_PSPass++;
         it_PAccept++;
      }
   } else {
      map<string, int>::iterator it_nLS_user = map_nLS_user.begin();
      map<string, int>::iterator it_L1Pass_user = map_L1Pass_user.begin();
      map<string, int>::iterator it_PSPass_user = map_PSPass_user.begin();
      map<string, int>::iterator it_PAccept_user = map_PAccept_user.begin();
      cout << "HLT path\t\t";
      if (print_nLS) cout << "nLS\t\t";
      if (print_L1Pass) cout << "L1Pass\t\t";
      if (print_PSPass) cout << "PSPass\t\t";
      if (print_PAccept) cout << "PAccept";
      cout << endl;
      for (it_nLS_user = map_nLS_user.begin(); it_nLS_user != map_nLS_user.end(); it_nLS_user++) {
         cout << it_nLS_user->first << "\t";
         if (print_nLS) cout << it_nLS_user->second << "\t";
         if (print_L1Pass) cout << it_L1Pass_user->second << "\t";
         if (print_PSPass) cout << it_PSPass_user->second << "\t";
         if (print_PAccept) cout << it_PAccept_user->second;
         cout << endl;
         it_L1Pass_user++;
         it_PSPass_user++;
         it_PAccept_user++;
      }
   }

   return 1;
}
