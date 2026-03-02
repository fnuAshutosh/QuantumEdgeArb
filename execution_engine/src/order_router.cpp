#include <iostream>
#include "order.h"
#include "risk.h"

bool route_order(const Order& order, double p_value) {
    RiskEngine risk;
    try {
        risk.check_risk(p_value);
        // log order as JSON-like text
        std::cout << "Routing order: " << order.order_id << "\n";
        return true;
    } catch (const std::exception& e) {
        std::cout << "Order rejected: " << e.what() << "\n";
        return false;
    }
}
