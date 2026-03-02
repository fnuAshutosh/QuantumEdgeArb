# Data Schemas

The system communicates via JSON messages encoded on Kafka topics, Step
Function events, and HTTP request/response bodies.  All producers and
consumers must adhere exactly to these schemas.

## 1. Tick (`ticks` topic)
```json
{
  "symbol":    "NVDA",
  "price":     123.45,
  "volume":    1000,
  "timestamp": 1700000000.0,
  "source":    "yfinance"
}
```

## 2. Signal (`signals` topic / Step Function input)
```json
{
  "pair":               "NVDA-TSM",
  "price_a":            123.45,
  "price_b":            87.60,
  "spread":             2.15,
  "zscore":            -2.31,
  "pvalue":             0.02,
  "coef_alpha":         5.10,
  "coef_beta":          1.34,
  "regime":             "Mean Reversion Opportunity",
  "regime_confidence":  0.91,
  "action":             "LONG_SPREAD",
  "timestamp":          1700000000.0
}
```

`action` values: `"LONG_SPREAD"` | `"SHORT_SPREAD"` | `"EXIT"` |
`"HOLD"` | `"KILL"`.

## 3. Order (input to `route_order()` and C++ OrderRouter)
```json
{
  "order_id":   "ord-uuid-001",
  "symbol":     "NVDA",
  "side":       "buy",
  "quantity":   8,
  "price":      123.45,
  "order_type": "market",
  "pair":       "NVDA-TSM",
  "leg":        "A",
  "timestamp":  1700000000.0
}
```

`side`: `"buy"` | `"sell"`.
`order_type`: `"market"` | `"limit"`.
`leg`: `"A"` | `"B"`.

## 4. Risk Event (output of `check_risk()`)
```json
{
  "order_id":   "ord-uuid-001",
  "type":       "kill_switch",
  "value":      0.07,
  "threshold":  0.05,
  "action":     "REJECT",
  "message":    "Cointegration p-value 0.07 exceeds kill threshold 0.05",
  "timestamp":  1700000000.0
}
```

`type`: `"ok"` | `"kill_switch"` | `"max_drawdown"` | `"position_limit"`.
`action`: `"APPROVE"` | `"REJECT"`.

## 5. NIM Request/Response (NVIDIA API)
REQUEST to `POST https://integrate.api.nvidia.com/v1/chat/completions`:
```json
{
  "model": "meta/llama-3.1-8b-instruct",
  "messages": [
    {
      "role": "system",
      "content": "You are a quantitative regime classifier. Given a z-score, classify the market regime as exactly one of: 'Mean Reversion Opportunity' or 'Structural Break'. Respond in JSON only: {\"regime\": \"...\", \"confidence\": 0.0}"
    },
    {
      "role": "user",
      "content": "Current z-score: -2.31. Cointegration p-value: 0.02. Classify regime."
    }
  ],
  "temperature": 0.1,
  "max_tokens": 50
}
```

RESPONSE:
```json
{
  "choices": [{
    "message": {
      "content": "{\"regime\": \"Mean Reversion Opportunity\", \"confidence\": 0.91}"
    }
  }]
}
```

## 6. SageMaker Endpoint Request/Response
POST to the endpoint defined by `SAGEMAKER_ENDPOINT_NAME` via
`boto3.runtime.invoke_endpoint()` with `Content-Type: application/json`.

**Request body:**
```json
{
  "prices_a": [100.1, 101.2, 102.3],
  "prices_b": [50.0, 50.5, 51.0]
}
```

**Response body:**
```json
{
  "coef":    [5.10, 1.34],
  "pvalue":  0.02,
  "zscore": -2.31,
  "residuals": [0.1, -0.2, 0.05]
}
```

## 7. FastAPI `/predict` Request/Response
POST `/predict` on `ml_model/deploy/api_server.py`.

**Request:**
```json
{
  "prices_a": [100.1, 101.2, 102.3, 103.4, 104.5],
  "prices_b": [50.0, 50.5, 51.0, 51.5, 52.0],
  "current_price_b": 52.5
}
```

**Response:**
```json
{
  "predicted_price_a": 105.6,
  "residual":          -0.31,
  "zscore":            -2.10,
  "pvalue":             0.03,
  "regime":            "Mean Reversion Opportunity",
  "regime_confidence":  0.89,
  "action":            "LONG_SPREAD"
}
```
