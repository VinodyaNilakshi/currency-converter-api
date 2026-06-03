export default async function handler(req, res) {
  const { from, to, amount } = req.query;

  if (!from || !to || !amount) {
    return res.status(400).json({
      error: "Please provide from, to, amount"
    });
  }

  const response = await fetch(
    `https://open.er-api.com/v6/latest/${from}`
  );

  const data = await response.json();

  const rate = data.rates[to];

  const converted = Number(amount) * rate;

  return res.json({
    from,
    to,
    amount: Number(amount),
    exchange_rate: rate,
    converted_amount: converted.toFixed(2)
  });
}
