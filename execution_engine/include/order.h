#pragma once

#include <string>

struct Order {
    std::string order_id;
    std::string symbol;
    std::string side;       // "buy" | "sell"
    double      quantity;
    double      price;
    std::string order_type; // "market" | "limit"
    std::string pair;
    std::string leg;        // "A" | "B"
    double      timestamp;
};
