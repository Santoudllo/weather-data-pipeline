#CQL pour initialiser la base de données Cassandra

echo "Waiting for Cassandra to start..."
sleep 30s

echo "Running CQL scripts..."
cqlsh cassandra -f /cassandra/init.cql
