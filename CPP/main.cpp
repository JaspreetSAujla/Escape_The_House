#include<iostream>
#include "EscapeHouseGame.h"
#include "EscapeHouseGame.cpp"
#include "HouseClass.h"
#include "HouseClass.cpp"
#include "ObjectClass.h"
#include "ObjectClass.cpp"
#include "PlayerClass.h"
#include "PlayerClass.cpp"
#include "RandomNumber.h"
#include "RandomNumber.cpp"
using namespace std;

int main() {
    EscapeHouseGame escapeHouseGame = EscapeHouseGame();
    escapeHouseGame.runGame();
}