from loguru import logger
import sys

logger.configure(
    handlers=[
        dict(sink='debug.log', colorize=True, mode='w'),
        dict(sink=sys.stdout),
    ]
)


def main():
    for i in range(10):
        logger.debug(i)


if __name__ == '__main__':
    main()
