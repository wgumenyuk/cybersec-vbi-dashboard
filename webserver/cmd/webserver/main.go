package main

import (
	"log"
	"net"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

const (
	port		= ":8080"
	staticDir	= "static"
)

func main() {
	fs := http.FileServer(http.Dir(staticDir))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		defer func() {
			var (
				ip string
				forwardedFor = r.Header.Get("X-Forwarded-For")
			)

			if len(forwardedFor) > 0 {
				ip = strings.Split(forwardedFor, ",")[0]
			} else {
				ip, _, _ = net.SplitHostPort(r.RemoteAddr)
			}

			log.Printf(
				"[%s] %s %s\n",
				ip,
				r.Method,
				r.URL.Path,
			)
		}()

		path := filepath.Join(staticDir, filepath.Clean(r.URL.Path))

		if _, err := os.Stat(path); os.IsNotExist(err) {
			http.ServeFile(w, r, filepath.Join(staticDir, "index.html"))
			return
		}

		fs.ServeHTTP(w, r)
	})

	log.Printf("Listening on port %s\n", port)

	if err := http.ListenAndServe(port, nil); err != nil {
		log.Fatal(err)
	}
}
