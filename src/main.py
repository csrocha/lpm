import argparse
import yaml
import publisher
import message
import logging
import glob

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument('config', type=argparse.FileType('r'), nargs='?',
                        help='Config file in YAML')
    parser.add_argument('--no-publish', dest='publish', action='store_false',
                        help='No publish the entries')
    parser.set_defaults(publish=True)

    args = parser.parse_args()
    configfile = args.config

    if configfile:
        logging.info("Loading configuration")

        configuration = yaml.load(configfile)

        for k, v in configuration.iteritems():
            logging.info("Processing %s", k)

            target = publisher.Publisher(v['server'], v['user'], v['password'])
            Message = message.dictMessage[v['parser']]

            for filename in glob.iglob(v['source']):
                logging.info("Reading file %s.", filename)
                with open(filename) as msgfile:
                    msg = Message(msgfile)
                    if args.publish:
                        target.pushEntries(msg.entries())
                    else:
                        for e in msg.entries():
                            logging.info("%s", e)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
