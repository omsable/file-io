# File.io for Asyncy

Ephemeral file sharing. Convenient, anonymous and secure via [file.io](https://file.io)

```sh
# usage.story
res = file-io data --expires 1w

# or a file
res = file-io `/path/to/image.png`
```

```js
res = {
  "success":true,
  "key":"aQbnDJ",
  "expiry":"7 days"
}
```

The file will be available at `https://file.io/aQbnDJ`.
