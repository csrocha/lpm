"""
Usage:

    lpm [config] {dir}

    Read files in directory, process and load them into system.

    config file in YAML:

        default:
            server: http://restServer
            source: file://test/emails
            user: hackaton
            password: jpmorgan
            system: ptp

"""
import argparse
import yaml
import publisher
import message
import os
import os.path
import logging

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument('config', type=argparse.FileType('r'), nargs='?',
                        help='Config file in YAML')

    args = parser.parse_args()
    configfile = args.config

    if configfile:
        logging.info("Loading configuration")

        configuration = yaml.load(configfile)

        for k, v in configuration.iteritems():
            logging.info("Processing %s", k)

            target = publisher.Publisher(v['server'], v['user'], v['password'])
            Message = message.dictMessage[v['parser']]
            for dirpath, dirnames, filenames in os.walk(v['source']):
                for filename in filenames:
                    with open(os.path.join(dirpath,filename)) as msgfile:
                        msg = Message(msgfile)
                        target.pushEntries(msg.entries())

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
