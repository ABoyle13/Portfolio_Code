#include "Item.h"

	// CONSTRUCTOR //
	Item::Item()
	{
		// will set the correct variable when an object is instantiated
		Item::setPrice(0);
		Item::setCalories(0);
	}

	// DESTRUCTOR //
	Item::~Item()
	{
		// delete item
	}

	// GETTERS //
	double Item::getPrice()
	{
		return Item::price;
	}
	int Item::getCalories()
	{
		return Item::calories;
	}

	// SETTERS //
	void Item::setName(std::string n)
	{
		Item::name = n;
	}
	void Item::setType(std::string a)
	{
		Item::type = a;
	}
	void Item::setPrice(double p)
	{
		Item::price = p;
	}
	void Item::setCalories(int c)
	{
		Item::calories = c;
	}

	// FUNCTIONS //

	std::string Item::toString()
	{
		std::string stuff;

		stuff.append(name);
		stuff.append(":  ");

		stuff.append(std::to_string(getPrice()));
		stuff.append("  ");

		stuff.append(std::to_string(getCalories()));
		stuff.append(" cal");

		return stuff;
	}

	//// Appetiser Class ////

	// CONSTRUCTOR //
	Appetiser::Appetiser(std::string line)
	{
		Appetiser::setShareable(false);
		Appetiser::setTwoForOne(false);
		Appetiser::setCalories(0);
		Appetiser::setPrice(0);

		// split string 'line'

		std::vector<std::string> tokens;
		std::stringstream check(line);
		std::string temp;

		while (getline(check, temp, ','))
		{
			tokens.push_back(temp);
		}
		
		Appetiser::setType(tokens[0]);
		Appetiser::setName(tokens[1]);
		Appetiser::setPrice(stod(tokens[2]));
		Appetiser::setCalories(stoi(tokens[3]));
		if (tokens[4] == "n")
		{Appetiser::setShareable(false);}
		else { Appetiser::setShareable(true);}
		if (tokens[5] == "n")
		{Appetiser::setTwoForOne(false);}
		else { Appetiser::setTwoForOne(true);}
	}

	// DESTRUCTOR //
	Appetiser::~Appetiser()
	{
		// delete item
	}

	// GETTERS //
	bool Appetiser::getShareable()
	{
		return Appetiser::shareable;
	}
	bool Appetiser::getTwoForOne()
	{
		return Appetiser::twoForOne;
	}

	// SETTERS //
	void Appetiser::setShareable(bool s)
	{
		Appetiser::shareable = s;
	}
	void Appetiser::setTwoForOne(bool t)
	{
		Appetiser::twoForOne = t;
	}

	// FUNCTIONS //
	std::string Appetiser::toString()
	{
		std::string stuff;
		double temp_price;
		int temp_cal;
		bool temp_bool;

		stuff.append(name);
		stuff.append(":  ");


		temp_price = getPrice();
		stuff.append(std::to_string(temp_price));
		stuff.append("  ");

		temp_cal = getCalories();
		stuff.append(std::to_string(temp_cal));
		stuff.append(" cal  ");

		temp_bool = getShareable();
		if (temp_bool == true)
		{
			stuff.append("(Shareable)");
		}
		temp_bool = getTwoForOne();
		if (temp_bool == true)
		{
			stuff.append("(2-4-1)");
		}

		return stuff;
	}

	//// Beverage Class ////

	// CONSTRUCTOR //
	Beverage::Beverage(std::string line)
	{
		Beverage::setVolume(0);
		Beverage::setABV(0.0);
		Beverage::setCalories(0);
		Beverage::setPrice(0);

		// split string 'line'

		std::vector<std::string> tokens;
		std::stringstream check(line);
		std::string temp;

		while (getline(check, temp, ','))
		{
			tokens.push_back(temp);
		}

		Beverage::setType(tokens[0]);
		Beverage::setName(tokens[1]);
		Beverage::setPrice(stod(tokens[2]));
		Beverage::setCalories(stoi(tokens[3]));
		Beverage::setVolume(stoi(tokens[6]));
		Beverage::setABV(stod(tokens[7]));
	}

	// DESTRUCTOR //
	Beverage::~Beverage()
	{
		// delete item
	}

	// GETTERS //
	int Beverage::getVolume()
	{
		return Beverage::volume;
	}
	double Beverage::getABV()
	{
		return Beverage::abv;
	}

	// SETTERS //
	void Beverage::setVolume(int v)
	{
		Beverage::volume = v;
	}
	void Beverage::setABV(double a)
	{
		Beverage::abv = a;
	}

	// FUNCTIONS //
	std::string Beverage::toString()
	{
		std::string stuff;
		double temp_price;
		int temp_cal;
		int temp_vol;
		double temp_abv;

		stuff.append(name);
		stuff.append(":  ");

		temp_price = getPrice();
		stuff.append(std::to_string(temp_price));
		stuff.append("  ");

		temp_cal = getCalories();
		stuff.append(std::to_string(temp_cal));
		stuff.append(" cal  (");

		temp_vol = getVolume();
		stuff.append(std::to_string(temp_vol));
		stuff.append("ml  ");

		temp_abv = getABV();
		stuff.append(std::to_string(temp_abv));
		stuff.append(" abv)");

		return stuff;
	}

	//// MainCourse Class ////

	// CONSTRUCTOR //
	MainCourse::MainCourse(std::string line)
	{
		MainCourse::setCalories(0);
		MainCourse::setPrice(0);

		// split string 'line'

		std::vector<std::string> tokens;
		std::stringstream check(line);
		std::string temp;

		while (getline(check, temp, ','))
		{
			tokens.push_back(temp);
		}

		MainCourse::setType(tokens[0]);
		MainCourse::setName(tokens[1]);
		MainCourse::setPrice(stod(tokens[2]));
		MainCourse::setCalories(stoi(tokens[3]));
	}

	// DESTRUCTOR //
	MainCourse::~MainCourse()
	{
		// delete item
	}

