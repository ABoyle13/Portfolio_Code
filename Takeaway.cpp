/* ------------------------------------------------------
CMP2801M: Advanced Programming
Driver program for "Takeaway" assignment
Autumn 2020

Written by James Brown

This file is a representative test file.
During marking, we will use the exact same notation
as provided in the brief, so make sure you follow that guideline.
Also make sure that you don't modify the code provided here,
but instead add what you need to complete the tasks.

Good luck!
------------------------------------------------------ */

//// AUTHOR: AOIFFE BOYLE (BOY19695525)
//// EXTENSION CODE: 2JJPWR7Y2RBD8WZG
//// SUBMISSION DATE: 28/01/2021
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cstring>
#include "Menu.h"
#include "Order.h"

using namespace std;

int main()
{
	string userCommand;
	vector <string> parameters;

	// Create a menu object from a CSV file
	Menu menu = Menu("menu.csv");
	Menu* mptr = &menu;

	// Create an order object
	Order order = Order();
	Order* optr = &order;

	std::cout << "Welcome to the Takeaway System." << std::endl;
	
	while (userCommand != "exit")
	{
		std::cout << "Please enter your desired command (menu, add, remove, checkout, help, exit): " << std::endl;
		getline(cin, userCommand);
		char* cstr = new char[userCommand.length() + 1];
		strcpy(cstr, userCommand.c_str());

		char* token;
		token = strtok(cstr, " ");
		string command;

		while (token != NULL)
		{
			parameters.push_back(token);
			token = strtok(NULL, " ");
		}

		if (parameters.size() < 1)
		{
			std::cout << "This is an invalid input - please try again" << std::endl;
		}
		else
		{
			command = parameters[0];
		}


		if (command.compare("menu") == 0) {
			std::cout << mptr->toString();
		}
		else if (command.compare("add") == 0)
		{
 			int num = stoi(parameters[1]);
			if (num > 12)
			{
				std::cout << "Invalid choice - please try again" << std::endl;
			}
			else if (num < 1)
			{
				std::cout << "Invalid choice - please try again" << std::endl;
			}
			else
			{
				tuple<std::string, Item*> choice = menu.option(num);
				std::string t = std::get<0>(choice);
				Item* x = std::get<1>(choice);
				optr->add(t, x);
			}
			// You may also wish to implement the ability to add multiple items at once!
			// e.g. add 1 5 9 
		}
		else if (command.compare("remove") == 0)
		{
			if (order.order.size() < 1)
			{
				std::cout << "Invalid choice - please try again" << std::endl;
			}
			else
			{
				int num = stoi(parameters[1]);
				if (num < 1)
				{
					std::cout << "Invalid choice - please try again" << std::endl;
				}
				else if (num > 12)
				{
					std::cout << "Invalid choice - please try again" << std::endl;
				}
				else
				{
					tuple<std::string, Item*> choice = menu.option(num);
					std::string t = std::get<0>(choice);
					Item* x = std::get<1>(choice);
					optr->remove(t, x);
				}
			}
		}
		else if (command.compare("checkout") == 0)
		{
			std::string info = optr->toString();
			std::cout << "Would you like to print your receipt or modify your order (1/2)" << std::endl;
			int input;
			cin >> input;
			if (input == 1)
			{
				order.printReceipt(info);
				break;
			}
			else if (input == 2)
			{

			}
		}
		else if (command.compare("help") == 0)
		{
			std::cout << "\n" << "Help Menu" << std::endl;
			std::cout << "Commands:" << std::endl;
			std::cout << "menu - to display the menu" << std::endl;
			std::cout << "add [number] - add an item to the order by index number" << std::endl;
			std::cout << "remove [number] - remove an item from the order by index number" << std::endl;
			std::cout << "checkout - displays the full order, with price and discout savings, and creates a receipt" << std::endl;
			std::cout << "help - to display the help menu" << std::endl;
			std::cout << "exit - to end the program" << "\n" << std::endl;
		}
		else if (command.compare("exit") == 0)
		{
			// deleting objects after use to free up memory space
			delete(mptr);
			delete(optr);
		}
		else 
		{
			
		}
		parameters.clear();
	}
	std::cout << "Press any key to quit...";
	std::getchar();

}