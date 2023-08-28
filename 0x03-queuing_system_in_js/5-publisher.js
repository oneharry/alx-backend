import { createClient, print } from 'redis';

const client = createClient();

client.on('error', err => {
    console.log(`Redis client not connected to the server: ${err}`);
})

client.on('connect', () => {
    console.log('Redis client connected to the server');
});


const publishMessage = (message, time) => {
    setTimeout(() => {
        console.log('About to send MESSAGE');
        client.publish('holberton school channel', message);
    }, time)
}

