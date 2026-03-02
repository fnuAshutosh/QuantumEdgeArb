#pragma once

class RiskEngine {
public:
    explicit RiskEngine(double kill_threshold = 0.05,
                        double max_position_usd = 1000.0);
    bool check_risk(double p_value) const;           // throws if p > threshold
    bool check_position_limit(double qty, double price) const;
private:
    double kill_threshold_;
    double max_position_usd_;
};
