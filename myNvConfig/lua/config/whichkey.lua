local M = {}

function M.setup()
    local whichkey = require "which-key"

    local conf = {
        window = {
            border = "single", -- none, single, double, shadow
            position = "bottom", -- bottom, top
        },
    }

    local opts = {
        mode = "n", -- Normal mode
        prefix = "<leader>",
        buffer = nil, -- Global mappings. Specify a buffer number for buffer local mappings
        silent = true, -- use `silent` when creating keymaps
        noremap = true, -- use `noremap` when creating keymaps
        nowait = false, -- use `nowait` when creating keymaps
    }

    local mappings = {
        ["s"] = { "<cmd>update!<CR>", "Save" },
        ["e"] = { "<cmd>NvimTreeToggle<cr>", "Explorer" },
        ["q"] = { "<cmd>q!<CR>", "Quit" },
        b = {
            name = "Buffer",
            c = { "<Cmd>bd!<Cr>", "Close current buffer" },
            D = { "<Cmd>%bd|e#|bd#<Cr>", "Delete all buffers" },
        },
        z = {
            name = "Packer",
            c = { "<cmd>PackerCompile<cr>", "Compile" },
            i = { "<cmd>PackerInstall<cr>", "Install" },
            s = { "<cmd>PackerSync<cr>", "Sync" },
            S = { "<cmd>PackerStatus<cr>", "Status" },
            u = { "<cmd>PackerUpdate<cr>", "Update" },
        },
        gs = {
            name = "Git",
            s = { "<cmd>Neogit<CR>", "Status" },
        },
        [" "] = { "<cmd>lua require('utils.finder').find_files()<cr>", "Files" },
        f = {
            name = "Find",
            --[""] = { "<cmd>lua require('utils.finder').find_files()<cr>", "Files" },
            d = { "<cmd>lua require('utils.finder').find_dotfiles()<cr>", "Dotfiles" },
            b = { "<cmd>Telescope buffers<cr>", "Buffers" },
            o = { "<cmd>Telescope oldfiles<cr>", "Old Files" },
            g = { "<cmd>Telescope live_grep<cr>", "Live Grep" },
            c = { "<cmd>Telescope commands<cr>", "Commands" },
            r = { "<cmd>Telescope file_browser<cr>", "Browser" },
            w = { "<cmd>Telescope current_buffer_fuzzy_find<cr>", "Current Buffer" },
            e = { "<cmd>NvimTreeToggle<cr>", "Explorer" },
        },
        c = {
            name = "Code",
            a = { "<cmd>lua vim.lsp.buf.code_action()<CR>", "Code Action" },
            d = { "<cmd>lua vim.diagnostic.open_float()<CR>", "Line Diagnostics" },
            i = { "<cmd>LspInfo<CR>", "Lsp Info" },
            ["[d"] = { "<cmd>lua vim.diagnostic.goto_prev()<CR>", "prev diag" },
            ["]d"] = { "<cmd>lua vim.diagnostic.goto_next()<CR>", "next diag" },
            ["[e"] = { "<cmd>lua vim.diagnostic.goto_prev({severity = vim.diagnostic.severity.ERROR})<CR>", "prev error" },
            ["]e"] = { "<cmd>lua vim.diagnostic.goto_next({severity = vim.diagnostic.severity.ERROR})<CR>", "next error" },
        },
        ["k"] = { "<cmd>lua vim.lsp.buf.hover()<CR>", "Hover" },
        g = {
            name = "Goto",
            d = { "<Cmd>lua vim.lsp.buf.definition()<CR>", "Definition" },
            D = { "<Cmd>lua vim.lsp.buf.declaration()<CR>", "Declaration" },
            s = { "<cmd>lua vim.lsp.buf.signature_help()<CR>", "Signature Help" },
            I = { "<cmd>lua vim.lsp.buf.implementation()<CR>", "Goto Implementation" },
            t = { "<cmd>lua vim.lsp.buf.type_definition()<CR>", "Goto Type Definition" },
            r = { "<cmd>lua vim.lsp.buf.references()<CR>", "Goto Type References" },
            n = { "<cmd>lua vim.lsp.buf.rename()<CR>", "Rename" },
            f = { "<cmd>lua vim.lsp.buf.format({ async=true})<CR> ", "Format" },
        }
    }

    whichkey.setup(conf)
    whichkey.register(mappings, opts)

    -- not start with leader key
    whichkey.register({ [""] = { "<cmd>NvimTreeToggle<cr>", "Explorer" }, }, { prefix = "<c-n>" })
end

return M
