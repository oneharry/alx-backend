import { createQueue } from 'kue';

const queue = createQuery();


const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

}

queue.process('push_notification_code', (job, done) => {
    const { message, phoneNumber } = job.data;
    sendNotification(phoneNumber, message);
    done();
})