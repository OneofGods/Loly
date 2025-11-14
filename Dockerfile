# 🔥💀 PHASE 2: PRODUCTION AUTONOMOUS AGENT SYSTEM 💀🔥
# Multi-stage Docker build for high-availability agent deployment

# =================== BUILDER STAGE ===================
FROM python:3.11-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create build directory
WORKDIR /build

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# =================== PRODUCTION STAGE ===================
FROM python:3.11-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    htop \
    procps \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Create application user for security
RUN useradd --create-home --shell /bin/bash agent_user

# Set working directory
WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /home/agent_user/.local

# Copy application code
COPY . /app/

# Create necessary directories with proper permissions
RUN mkdir -p /app/logs \
             /app/data \
             /app/ml_models \
             /app/tmp \
             /app/config \
    && chown -R agent_user:agent_user /app \
    && chmod 755 /app/logs /app/data /app/ml_models /app/tmp

# Switch to application user
USER agent_user

# Add local packages to PATH
ENV PATH="/home/agent_user/.local/bin:$PATH"

# Environment variables for production
ENV PYTHONPATH="/app"
ENV PYTHONUNBUFFERED=1
ENV AGENT_ENVIRONMENT="production"
ENV LOG_LEVEL="INFO"
ENV MESSAGE_BUS_HOST="0.0.0.0"
ENV MESSAGE_BUS_PORT="8080"
ENV METRICS_PORT="8081"
ENV HEALTH_CHECK_PORT="8082"

# Expose ports
EXPOSE 3005 8080 8081 8082

# Health check for autonomous agent system
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8082/health || curl -f http://localhost:3005/health || exit 1

# Default command - can be overridden for different services
CMD ["python", "run_agent_system.py"]