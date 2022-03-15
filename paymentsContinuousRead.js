const { MongoClient } = require('mongodb');
const Chance = require('chance');

const DATABASE = "UPS";
const COLLECTION = "payments";
const chance = new Chance();
let continueRead = true;

async function main() {
    const arguments = process.argv.slice(2);
    let retry = false;

    if (arguments.length > 0) {
        retry = (arguments[0].toLowerCase() === "retry")
    }

    const uri = `mongodb+srv://pleury:YSBWDKthfqPaQR6O@m10cluster.kljfx.mongodb.net/myFirstDatabase?retryReads=${retry}`;
    const client = new MongoClient(uri);
    console.log(`Retry = ${retry}`);

    try {
        await client.connect();
        await readDocuments(client);
    }
    catch (error) {
        console.error(error);
    }
    finally {
        await client.close();
    }
}

main().catch(console.error);

async function readDocuments(client) {
    let count = 0;
    let connectionIssue = false;

    while (continueRead) {
        try {
            count++;

            let highest = await client.db(DATABASE).collection(COLLECTION).findOne({}, { sort: { paymentNumber: -1 }, limit: 1 });

            if (count % 30 == 0) {
                console.log(`${new Date().toISOString()} - Read Count=${count}  Highest Payment Number=${highest.paymentNumber}`);
            }

            if (connectionIssue) {
                console.log(`${new Date().toISOString()} - RECONNECTED-TO-DB`);
                connectionIssue = false;
            }
        }
        catch (error) {
            console.log(`${new Date().toISOString()} - DB-CONNECTION-PROBLEM`);
            console.log(error);
            connectionIssue = true;
        }
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

process.on('SIGINT', function () {
    continueRead = false;
});


