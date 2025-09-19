
#!/usr/bin/env bash
# wait-for-service.sh host:port - waits until TCP port is open
set -e

hostport=$1

IFS=':' read -ra hp <<< "$hostport"
host=${hp[0]}
port=${hp[1]}

until nc -z "$host" "$port"; do
  echo "Waiting for $host:$port..."
  sleep 0.5
done

echo "$host:$port is available"


chmod +x scripts/wait-for-service.sh
