#pragma once
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <tuple>

class Item
{
private:
	// VARIABLES //
	double price;
	int calories;

public:
	// VARIABLES //
	std::string type;
	std::string name;

	// CONSTRUCTOR //
	Item();

	// DESTRUCTOR //
	virtual ~Item();

	// GETTERS //
	double getPrice();
	int getCalories();

	// SETTERS //
	void setName(std::string);
	void setType(std::string);
	void setPrice(double);
	void setCalories(int);

	// FUNCTIONS //
	virtual std::string toString();
};

//// Appetiser Class ////

class Appetiser : public Item
{
private:
	// VARIABLES //
	bool shareable;
	bool twoForOne;

public:
	// CONSTRUCTOR //
	Appetiser(std::string);

	// DESTRUCTOR //
	virtual ~Appetiser();

	// GETTERS //
	bool getShareable();
	bool getTwoForOne();

	// SETTERS //
	void setShareable(bool);
	void setTwoForOne(bool);

	// FUNCTIONS //
	virtual std::string toString();
};

//// Beverage Class ////

class Beverage : public Item
{
private:
	// VARIABLES //
	int volume;
	double abv;

public:
	// CONSTRUCTOR //
	Beverage(std::string);

	// DESTRUCTOR //
	virtual ~Beverage();

	// GETTERS //
	int getVolume();
	double getABV();

	// SETTERS //
	void setVolume(int);
	void setABV(double);

	// FUNCTIONS //
	virtual std::string toString();
};

//// MainCourse Class ////

class MainCourse : public Item
{
public:
	// CONSTRUCTOR //
	MainCourse(std::string);

	// DESTRUCTOR //
	virtual ~MainCourse();

	// NO NEW VARIABLES //
	// No toString - MainCourse Items will use Item::toString()
};

//// ItemList Class ////

class ItemList
{
	//// ABSTRACT CLASS ////

public:
	// VECTOR //
	std::vector<Item*> items;

	// PURE VIRTUAL FUNCTION //
	virtual std::string toString() = 0;
};

