#include "Item.h"
#include <tuple>
#include <fstream>
#include <iostream>

class Order : public ItemList
{
public:
	// VARIABLES //
	std::vector<std::tuple<std::string, Item*>> order;
	std::tuple<std::string, Item*> temp;
	double total;
	double savings;
	std::string info;

	// CONSTRUCTOR //
	Order();

	// FUNCTIONS //
	void add(std::string, Item*);
	void remove(std::string, Item*);
	void CalculateTotal();
	std::string toString();
	void printReceipt(std::string);
};
