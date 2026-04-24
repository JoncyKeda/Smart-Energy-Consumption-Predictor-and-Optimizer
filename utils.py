def suggest_optimization(consumption):
    if consumption > 700:
        return "⚠️ High usage detected. Avoid heavy appliances during peak hours."
    elif consumption > 400:
        return "⚡ Moderate usage. Try shifting usage to off-peak hours."
    else:
        return "✅ Efficient usage. Good energy management!"
