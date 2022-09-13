FROM golang:1.18 AS builder

WORKDIR /app
RUN git clone https://github.com/ledgerwatch/erigon.git
RUN cd erigon && git checkout alpha && make erigon

FROM golang:1.18 AS runtime
COPY --from=builder /app/erigon/build/bin/erigon /usr/local/bin/erigon

EXPOSE 8545 \
       8551 \
       8546 \
       30303 \
       30303/udp \
       42069 \
       42069/udp \
       8080 \
       9090 \
       6060

CMD ["erigon"]
