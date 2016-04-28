#!/usr/bin/env python3
# coding: utf-8
# Lab 7 - Server
# François Chalifour

from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from json import dumps

from api import *
from utils import Colors


SERVER_ADDRESS = (HOST, PORT) = 'localhost', 5000


class RequestHandler(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def do_GET(self):
        self.set_headers()

        if self.path.startswith('/humans'):
            all_params = self.path.split('/')
            valid_params = [ p for p in all_params if p ]

            if len(valid_params) > 1:
                id = valid_params[1]
                if id.isdigit():
                    human_id = int(id)
                    if human_id in humans:
                        query = humans.get(human_id)
                        result = query.get('name')
                    else:
                        query = human_not_found
                        result = 'unknown human'
                else:
                    query = resource_not_found
                    result = 'unknown human'
            else:
                query = humans
                result = ', '.join([ h.get('name') for h in query.values() ])

            self.wfile.write(dumps(
                query,
                sort_keys = True,
                indent = 4,
                ensure_ascii=False,
            ).encode('utf-8'))

            print(
                '[{green}{time}{default}] Get {blue}{humans}{default}'
                .format(
                    time=datetime.now().strftime('%H:%M:%S'),
                    humans=result,
                    green=Colors.GREEN,
                    blue=Colors.BLUE,
                    default=Colors.DEFAULT,
                )
            )

        elif self.path.startswith('/compute'):
            url = urlparse(self.path)
            query = url.query
            data = parse_qs(query)
            fields = ['left-operand', 'operation', 'right-operand']

            if all([ f in data for f in fields ]):
                left_operand = int(data['left-operand'][0])
                operation = data['operation'][0]
                right_operand = int(data['right-operand'][0])

                if operation in commands.keys():
                    result = commands[operation](left_operand, right_operand)

                    self.wfile.write(dumps(
                        {
                            "query": "{} {} {}".format(left_operand, operation, right_operand),
                            "result": "{}".format(result)
                        },
                        sort_keys = True,
                        indent = 4,
                        ensure_ascii=False,
                    ).encode('utf-8'))

                    print(
                        '[{green}{time}{default}] Compute {blue}{left_operand} {operation} {right_operand} = {result}{default}'
                        .format(
                            time=datetime.now().strftime('%H:%M:%S'),
                            left_operand=left_operand,
                            operation=operation,
                            right_operand=right_operand,
                            result=result,
                            green=Colors.GREEN,
                            blue=Colors.BLUE,
                            default=Colors.DEFAULT,
                        )
                    )
                else:
                    self.wfile.write(dumps(
                        wrong_values,
                        sort_keys = True,
                        indent = 4,
                        ensure_ascii=False,
                    ).encode('utf-8'))

                    print(
                        '[{green}{time}{default}] Compute error: {fail}wrong values{default}'
                        .format(
                            time=datetime.now().strftime('%H:%M:%S'),
                            green=Colors.GREEN,
                            fail=Colors.FAIL,
                            default=Colors.DEFAULT,
                        )
                    )

            else:
                self.wfile.write(dumps(
                    missing_params,
                    sort_keys = True,
                    indent = 4,
                    ensure_ascii=False,
                ).encode('utf-8'))

                print(
                    '[{green}{time}{default}] Compute error: {fail}missing params{default}'
                    .format(
                        time=datetime.now().strftime('%H:%M:%S'),
                        green=Colors.GREEN,
                        fail=Colors.FAIL,
                        default=Colors.DEFAULT,
                    )
                )

        else:
            self.wfile.write(dumps(
                resource_not_found,
                sort_keys = True,
                indent = 4,
                ensure_ascii=False,
            ).encode('utf-8'))


if __name__ == '__main__':
    try:
        server = HTTPServer(SERVER_ADDRESS, RequestHandler)

        print(
            '[{green}{time}{default}] Webserver started at {blue}http://{host}:{port}{default}'
            .format(
                time=datetime.now().strftime('%H:%M:%S'),
                host=HOST,
                port=PORT,
                green=Colors.GREEN,
                blue=Colors.BLUE,
                default=Colors.DEFAULT,
            )
        )

        server.serve_forever()

    except KeyboardInterrupt:
        print(
            '{warning}Shutting down the web server...{default}'
            .format(
                warning=Colors.WARNING,
                default=Colors.DEFAULT,
            )
        )
