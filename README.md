cat > README.md <<'EOF'
# Simple Interest Calculator (Bash)

A tiny Bash script to compute **Simple Interest**:

\[
\text{SI} = \frac{P \times R \times T}{100}
\]

- `P` = Principal (amount)
- `R` = Annual interest rate (percent)
- `T` = Time (years)

## Quick Start

```bash
# Make executable
chmod +x simple-interest.sh

# Use with command-line args:
./simple-interest.sh 10000 7.5 3

# Or run and follow prompts:
./simple-interest.sh
