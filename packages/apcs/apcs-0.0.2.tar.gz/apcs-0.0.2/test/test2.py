from apcs import Config

def main():
    parser, cfg = Config.auto_argparser()
    args = parser.parse_args()
    cfg.merge_from_options(args)
    
    print(cfg.gpus)
    print(cfg.model_kwargs)

if __name__ == '__main__':
    main()