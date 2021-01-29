#include "Menu.h"
#include <sstream>

// CONSTRUCTORS //
Menu::Menu(string filename)
{ 
	// HOLDER VARIABLE //
	string line;

	// Item object pointer 
	Item* store;

	ifstream myFile (filename);

	while (getline(myFile, line))
	{
		// check what type each menu item is
		if (line[0] == 'a')
		{
			store = new Appetiser(line);
			items.push_back(store);
		}
		else if (line[0] == 'm')
		{
			store = new MainCourse(line);
			items.push_back(store);
		}
		else if (line[0] == 'b')
		{
			store = new Beverage(line);
			items.push_back(store);
		}
	}
}

// FUNCTIONS //
void Menu::add()
{

}

string Menu::toString()
{
	// sort vector of item pointers and display to user
	tuple <string, Item*> info;
	std::vector<Item*> app;
	std::vector<Item*> main;
	std::vector<Item*> bev;

	for (int d = 0; d < items.size(); d++)
	{
		std::string typeName = items[d]->type;
		info = make_tuple(typeName, items[d]);
		sorted.push_back(info);
	}

	std::sort(sorted.begin(), sorted.end());

	//// Print Menu to user ////
	//std::cout << "----------------------Appetisers---------------------" << std::endl;
	
	std::string access;
	std::string output;
	Item* temp;
	int count = 1;

	for (int h = 0; h < sorted.size(); h++)
	{
		temp = std::get<1>(sorted[h]);
		access = temp->toString();
		output.append("(");
		output.append(to_string(count));
		output.append(") ");
		output.append(access);
		output.append("\n");
		count++;
	}
	
	return output;
}

tuple<std::string, Item*> Menu::option(int num)
{
	return sorted[num - 1];
}