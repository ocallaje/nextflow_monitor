FROM rust:1.78 AS build
WORKDIR /usr/src/wsserver

COPY . .

RUN make

FROM debian:bookworm
WORKDIR /usr/local/bin

COPY --from=build /usr/src/wsserver/target/release/wsserver .

EXPOSE 8080

CMD ["./wsserver"]