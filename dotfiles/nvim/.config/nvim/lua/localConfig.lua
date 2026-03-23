local M = {}
function M.setup()
  local bemol_dir = vim.fs.find({ '.bemol' }, { upward = true, type = 'directory' })[1]
  local ws_folders_lsp = {}
  if bemol_dir then
    local file = io.open(bemol_dir .. '/ws_root_folders', 'r')
    if file then
      for line in file:lines() do
        table.insert(ws_folders_lsp, line)
      end
      file:close()
    end
  end

  for _, line in ipairs(ws_folders_lsp) do
    vim.lsp.buf.add_workspace_folder(line)
  end
end

return M
