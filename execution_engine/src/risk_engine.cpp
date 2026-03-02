#include <stdexcept>
#include "risk.h"

RiskEngine::RiskEngine(double kill_threshold, double max_position_usd)
    : kill_threshold_(kill_threshold), max_position_usd_(max_position_usd) {}

bool RiskEngine::check_risk(double p_value) const {
    if (p_value > kill_threshold_) {
        throw std::runtime_error("kill switch: p-value too high");
    }
    return false;
}

bool RiskEngine::check_position_limit(double qty, double price) const {
    double notional = qty * price;
    if (notional > max_position_usd_) {
        throw std::runtime_error("position limit exceeded");
    }
    return false;
}
