FROM node:23-slim AS node-builder
WORKDIR /opt/app
COPY ./ ./
RUN npm install -g pnpm
RUN pnpm install && pnpm build

FROM golang:1.23 AS go-builder
WORKDIR /opt/webserver
COPY webserver/ ./
RUN GOOS=linux CGO_ENABLED=0 go build -v -o build/webserver cmd/webserver/main.go

FROM alpine:latest
WORKDIR /opt/vbi
COPY --from=node-builder /opt/app/build static/
COPY --from=go-builder /opt/webserver/build ./
EXPOSE 8080
ENTRYPOINT [ "/opt/vbi/webserver" ]
