const kue = require('kue');
const jobInfo = {
  phoneNumber: '+1221542345',
  message: 'Hello, this is a test message.'
};
const queue = kue.createQueue();
const jobOffer = queue.create('push_notification_code', jobInfo).save(err=> {
	if (!err) {
		console.log(`Notification job created: ${job.id}`);
	}
});
jobOffer.on('complete', () => {
	console.log('Notification job completed');
});
jobOffer.on('error', () => {
	console.log('Notification job failed');
});
