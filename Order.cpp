#include "Order.h"

Order::Order()
{
	total = 0;
	savings = 0;
}
void Order::add(std::string t, Item* choice)
{
	temp = make_tuple(t, choice);

	order.push_back(temp);

	double priceFound;
	std::cout << "Adding item..." << std::endl;
	std::cout << std::get<1>(temp)->toString() << std::endl;
	priceFound = std::get<1>(temp)->getPrice();
	total = total + priceFound;
	std::cout << "\n" << std::endl;

	CalculateTotal();
}
void Order::remove(std::string t, Item* choice)
{
	temp = make_tuple(t, choice);
	
	auto i = find(order.begin(), order.end(), temp);
	int v = std::get<1>(*i)->getPrice();
	total -= v;

	std::cout << "Removing item..." << std::endl;
	order.erase(i);

	for (int j = 0; j < order.size(); j++)
	{
		std::cout << std::get<1>(order[j])->toString() << std::endl;
	}
	std::cout << "\n" << std::endl;

	CalculateTotal();
}

void Order::CalculateTotal()
{
	std::cout << "Your Order" << std::endl;
	
	int app = 0;
	std::string info;
	double found;
	
	for (int g = 0; g < order.size(); g++)
	{
		std::cout << std::get<1>(order[g])->toString() << std::endl;
		if (std::get<0>(order[g]) == "a")
		{
			info = std::get<1>(order[g])->toString();
			if (info.find("(2") != std::string::npos)
			{
				app++;
			}
			if (app == 2)
			{
				found = std::get<1>(order[g])->getPrice();
				savings = found;
				std::cout << "2-4-1 Offer: discount -" << found << "\n" << std::endl;
				total -= found;
			}
		}
	}
	std::cout << "\n" << std::endl;
}

std::string Order::toString()
{
	std::string line;
	std::cout << "\n" << "Your Order" << std::endl;
	info.append("Your Order \n");
	for (int k = 0; k < order.size(); k++)
	{
		line = std::get<1>(order[k])->toString();
		std::cout << line << std::endl;
		info.append(line + "\n");
	}
	std::cout << "Savings: " << savings << std::endl;
	info.append("Savings: " + std::to_string(savings) + "\n");
	std::cout << "Total: " << total << std::endl;
	info.append("Total: " + std::to_string(total) + "\n");

	return info;
}

void Order::printReceipt(std::string info)
{
	// read into file
	std::ofstream myFile;
	myFile.open("receipt.txt", std::ofstream::trunc);
	myFile << info;
	myFile.close();
}