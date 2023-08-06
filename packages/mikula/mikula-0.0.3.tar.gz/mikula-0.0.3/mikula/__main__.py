from mikula.implementation.cli import create_parser

parser = create_parser()
args = parser.parse_args()

if "function" in args:
    command = args.function
    delattr(args, "function")
    kwargs = vars(args)
    command(**kwargs)
