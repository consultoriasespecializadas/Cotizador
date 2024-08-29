def calculate_cost(kwh_per_month):
    # System size in kWp (this is a simple calculation based on kWh)
    system_size = kwh_per_month / 150  # Assuming 150 kWh per kWp

    # Cost per kWp
    cost_per_kwp = 6443000  # Example cost in your currency

    # Total cost
    total_cost = system_size * cost_per_kwp

    # Add VAT (12%)
    vat = total_cost * 0.12

    # Final total
    final_total = total_cost + vat

    return system_size, total_cost, vat, final_total

# Example usage
kwh_per_month = float(input("Enter your monthly energy consumption in kWh: "))
system_size, total_cost, vat, final_total = calculate_cost(kwh_per_month)

print(f"System Size: {system_size:.2f} kWp")
print(f"Total Cost: {total_cost:.2f}")
print(f"VAT: {vat:.2f}")
print(f"Final Total: {final_total:.2f}")
