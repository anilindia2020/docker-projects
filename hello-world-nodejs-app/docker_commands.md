cd hello-world-nodejs-app

$ docker build -t hello-world-node-app .

$ docker run --name my-running-app -p 3000:3000 -d hello-world-node-app

Go to http://localhost:3000 in your browser. You'll see your message!

Key Concepts learnt:

Dockerfile: The recipe for building your own Docker image.

FROM, WORKDIR, COPY, RUN, EXPOSE, CMD: Core Dockerfile instructions.

docker build: The command to create an image from a Dockerfile.

-t my-node-app (Tagging): Giving your image a memorable name.
