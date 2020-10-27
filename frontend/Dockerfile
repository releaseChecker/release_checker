FROM node:12.18.3

COPY . .
RUN chmod +x entrypoint.sh
RUN yarn
ENTRYPOINT ["./entrypoint.sh"]