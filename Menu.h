#include <fstream>
#include "Item.h"

using namespace std;

class Menu : public ItemList
{
public:
	// VARIABLES //
	string name;
	std::vector<tuple<std::string, Item*>> sorted;

	// CONSTRUCTOR //
	Menu(string);

	// FUNCTIONS //
	void add();
	string toString();
	tuple<std::string, Item*> option(int);
};