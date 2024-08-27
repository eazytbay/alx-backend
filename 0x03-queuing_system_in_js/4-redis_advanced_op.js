import { createClient } from 'redis';
const redis = require('redis');
const client = createClient({
host: 'localhost',
port: 6379,
});

client.hset('HolbertonSchools', 'Portland', '50', redis.print);
client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
client.hset('HolbertonSchools', 'New York', '20', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '40', redis.print);
client.hset('HolbertonSchools', 'Paris', '2', redis.print);
client.hgetall('HolbertonSchools', (err, res) => {
if (err) {
	console.error(err);
}
	else {
		console.log(res);
	}
});
