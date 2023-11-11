# Dockerfile
FROM node:14 as builder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .

FROM python:3.8
WORKDIR /app
COPY --from=builder /app .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["npm", "start"]
